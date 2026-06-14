"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_summary

ApplicationsList: TypeAlias = list["aws_sdk_appintegrations.types.application_summary.ApplicationSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationsList) -> list:
    import aws_sdk_appintegrations.types.application_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_appintegrations.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationsList:
    import aws_sdk_appintegrations.types.application_summary
    out: ApplicationsList = []
    for item in data:
        out.append(aws_sdk_appintegrations.types.application_summary.deserialize_json(item))
    return out