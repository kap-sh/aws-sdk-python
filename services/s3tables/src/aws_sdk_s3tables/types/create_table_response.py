"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.version_token


class CreateTableResponse(TypedDict, closed=True):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTableResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    out["versionToken"] = value["version_token"]
    return out


def deserialize_json(data: dict) -> CreateTableResponse:
    out: CreateTableResponse = {}  # type: ignore[typeddict-item]
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError("CreateTableResponse.table_arn required")
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError("CreateTableResponse.version_token required")
    return out
