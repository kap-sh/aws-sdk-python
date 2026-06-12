"""Generated from Smithy shape ``com.amazonaws.configservice#ExecutionControls``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.ssm_controls


class ExecutionControls(TypedDict):
    ssm_controls: NotRequired["aws_sdk_config_service.types.ssm_controls.SsmControls"]
    """<p>A SsmControls object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionControls) -> dict:
    out: dict = {}
    if "ssm_controls" in value:
        import aws_sdk_config_service.types.ssm_controls

        out["SsmControls"] = (
            aws_sdk_config_service.types.ssm_controls.serialize_aws_json_1_1(
                value["ssm_controls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionControls:
    out: ExecutionControls = {}  # type: ignore[typeddict-item]
    if "SsmControls" in data:
        import aws_sdk_config_service.types.ssm_controls

        out["ssm_controls"] = (
            aws_sdk_config_service.types.ssm_controls.deserialize_aws_json_1_1(
                data["SsmControls"]
            )
        )
    return out
