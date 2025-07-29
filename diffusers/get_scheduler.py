def get_scheduler(
    scheduler_name,
    scheduler_config,
):
    if scheduler_name == 'Euler A':
        from diffusers.schedulers import EulerAncestralDiscreteScheduler
        scheduler = EulerAncestralDiscreteScheduler.from_config(scheduler_config)
    elif scheduler_name == 'UniPC':
        from diffusers.schedulers import UniPCMultistepScheduler
        scheduler = UniPCMultistepScheduler.from_config(scheduler_config)
    elif scheduler_name == 'Euler':
        from diffusers.schedulers import EulerDiscreteScheduler
        scheduler = EulerDiscreteScheduler.from_config(scheduler_config)
    elif scheduler_name == 'DDIM':
        from diffusers.schedulers import DDIMScheduler
        scheduler = DDIMScheduler.from_config(scheduler_config)
    elif scheduler_name == 'DDPM':
        from diffusers.schedulers import DDPMScheduler
        scheduler = DDPMScheduler.from_config(scheduler_config)
    else:
        raise ValueError(f"Unknown scheduler: {scheduler_name}")
    return scheduler