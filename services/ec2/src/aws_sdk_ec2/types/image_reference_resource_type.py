"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReferenceResourceType``."""

from typing import Literal, TypeAlias

ImageReferenceResourceType: TypeAlias = Literal[
    "ec2:Instance",
    "ec2:LaunchTemplate",
    "ssm:Parameter",
    "imagebuilder:ImageRecipe",
    "imagebuilder:ContainerRecipe",
]
