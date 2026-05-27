"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateErrorCode``."""

from typing import Literal, TypeAlias

LaunchTemplateErrorCode: TypeAlias = Literal[
    "launchTemplateIdDoesNotExist",
    "launchTemplateIdMalformed",
    "launchTemplateNameDoesNotExist",
    "launchTemplateNameMalformed",
    "launchTemplateVersionDoesNotExist",
    "unexpectedError",
]
