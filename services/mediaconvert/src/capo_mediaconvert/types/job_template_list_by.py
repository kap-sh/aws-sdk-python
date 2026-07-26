"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobTemplateListBy``."""

from typing import Literal, TypeAlias, cast

"""Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name."""
JobTemplateListBy: TypeAlias = Literal[
    "NAME",
    "CREATION_DATE",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplateListBy) -> str:
    return value


def deserialize_json(data: str) -> JobTemplateListBy:
    return cast(JobTemplateListBy, data)
