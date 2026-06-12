"""Generated from Smithy shape ``com.amazonaws.lightsail#StopGUISessionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.operation_list


class StopGUISessionResult(TypedDict):
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>The available API operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGUISessionResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGUISessionResult:
    out: StopGUISessionResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
