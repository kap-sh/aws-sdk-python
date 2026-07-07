"""Generated from Smithy shape ``com.amazonaws.lightsail#StartRelationalDatabaseResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.operation_list


class StartRelationalDatabaseResult(TypedDict, closed=True):
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRelationalDatabaseResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRelationalDatabaseResult:
    out: StartRelationalDatabaseResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
