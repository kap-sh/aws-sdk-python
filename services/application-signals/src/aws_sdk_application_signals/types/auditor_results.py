"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditorResults``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_application_signals.types.auditor_result

AuditorResults: TypeAlias = list["aws_sdk_application_signals.types.auditor_result.AuditorResult"]


# --- restJson1 ser/de ---
def serialize_json(value: AuditorResults) -> list:
    import aws_sdk_application_signals.types.auditor_result
    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.auditor_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditorResults:
    import aws_sdk_application_signals.types.auditor_result
    out: AuditorResults = []
    for item in data:
        out.append(aws_sdk_application_signals.types.auditor_result.deserialize_json(item))
    return out