"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.connection


class DeleteConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["capo_apprunner.types.connection.Connection"]
    """<p>A description of the App Runner connection that this request just deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_apprunner.types.connection

        out["Connection"] = capo_apprunner.types.connection.serialize_aws_json_1_0(
            value["connection"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionResponse:
    out: DeleteConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_apprunner.types.connection

        out["connection"] = capo_apprunner.types.connection.deserialize_aws_json_1_0(
            data["Connection"]
        )
    return out
