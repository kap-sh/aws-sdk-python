"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DatabaseConfigDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class DatabaseConfigDetail(TypedDict, closed=True):
    secret_name: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> AWS Secrets Manager key that holds the credentials that you use to connect to a database. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseConfigDetail) -> dict:
    out: dict = {}
    if "secret_name" in value:
        out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> DatabaseConfigDetail:
    out: DatabaseConfigDetail = {}  # type: ignore[typeddict-item]
    if "secretName" in data:
        out["secret_name"] = data["secretName"]
    return out
