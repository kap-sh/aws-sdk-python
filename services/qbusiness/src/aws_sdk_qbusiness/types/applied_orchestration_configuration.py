"""Generated from Smithy shape ``com.amazonaws.qbusiness#AppliedOrchestrationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.orchestration_control


class AppliedOrchestrationConfiguration(TypedDict):
    control: "aws_sdk_qbusiness.types.orchestration_control.OrchestrationControl"
    """<p> Information about whether chat orchestration is enabled or disabled for an Amazon Q Business application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppliedOrchestrationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.orchestration_control

    out["control"] = aws_sdk_qbusiness.types.orchestration_control.serialize_json(
        value["control"]
    )
    return out


def deserialize_json(data: dict) -> AppliedOrchestrationConfiguration:
    out: AppliedOrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import aws_sdk_qbusiness.types.orchestration_control

        out["control"] = aws_sdk_qbusiness.types.orchestration_control.deserialize_json(
            data["control"]
        )
    else:
        raise DeserializationError("AppliedOrchestrationConfiguration.control required")
    return out
