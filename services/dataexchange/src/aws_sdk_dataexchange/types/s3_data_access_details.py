"""Generated from Smithy shape ``com.amazonaws.dataexchange#S3DataAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of__string


class S3DataAccessDetails(TypedDict, closed=True):
    key_prefixes: NotRequired[
        "aws_sdk_dataexchange.types.list_of__string.ListOf__string"
    ]
    """<p>A list of the key prefixes affected by this notification. This can have up to 50 entries.</p>"""
    keys: NotRequired["aws_sdk_dataexchange.types.list_of__string.ListOf__string"]
    """<p>A list of the keys affected by this notification. This can have up to 50 entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataAccessDetails) -> dict:
    out: dict = {}
    if "key_prefixes" in value:
        import aws_sdk_dataexchange.types.list_of__string

        out["KeyPrefixes"] = aws_sdk_dataexchange.types.list_of__string.serialize_json(
            value["key_prefixes"]
        )
    if "keys" in value:
        import aws_sdk_dataexchange.types.list_of__string

        out["Keys"] = aws_sdk_dataexchange.types.list_of__string.serialize_json(
            value["keys"]
        )
    return out


def deserialize_json(data: dict) -> S3DataAccessDetails:
    out: S3DataAccessDetails = {}  # type: ignore[typeddict-item]
    if "KeyPrefixes" in data:
        import aws_sdk_dataexchange.types.list_of__string

        out["key_prefixes"] = (
            aws_sdk_dataexchange.types.list_of__string.deserialize_json(
                data["KeyPrefixes"]
            )
        )
    if "Keys" in data:
        import aws_sdk_dataexchange.types.list_of__string

        out["keys"] = aws_sdk_dataexchange.types.list_of__string.deserialize_json(
            data["Keys"]
        )
    return out
