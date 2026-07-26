"""Generated from Smithy shape ``com.amazonaws.lightsail#StopGUISessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.operation_list


class StopGUISessionResult(TypedDict, closed=True):
    operations: NotRequired["capo_lightsail.types.operation_list.OperationList"]
    """<p>The available API operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGUISessionResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_lightsail.types.operation_list

        out["operations"] = capo_lightsail.types.operation_list.serialize_aws_json_1_1(
            value["operations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGUISessionResult:
    out: StopGUISessionResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import capo_lightsail.types.operation_list

        out["operations"] = (
            capo_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
