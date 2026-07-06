"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateRelationalDatabaseResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.operation_list


class CreateRelationalDatabaseResult(TypedDict, closed=True):
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRelationalDatabaseResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRelationalDatabaseResult:
    out: CreateRelationalDatabaseResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
