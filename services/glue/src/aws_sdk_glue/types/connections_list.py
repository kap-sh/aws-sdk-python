"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionsList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_string_list


class ConnectionsList(TypedDict):
    connections: NotRequired[
        "aws_sdk_glue.types.connection_string_list.ConnectionStringList"
    ]
    """<p>A list of connections used by the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionsList) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_glue.types.connection_string_list

        out["Connections"] = (
            aws_sdk_glue.types.connection_string_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionsList:
    out: ConnectionsList = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_glue.types.connection_string_list

        out["connections"] = (
            aws_sdk_glue.types.connection_string_list.deserialize_aws_json_1_1(
                data["Connections"]
            )
        )
    return out
