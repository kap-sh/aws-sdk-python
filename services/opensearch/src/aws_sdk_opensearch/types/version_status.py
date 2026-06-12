"""Generated from Smithy shape ``com.amazonaws.opensearch#VersionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.option_status
    import aws_sdk_opensearch.types.version_string


class VersionStatus(TypedDict):
    options: "aws_sdk_opensearch.types.version_string.VersionString"
    """<p>The OpenSearch or Elasticsearch version for the specified domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of the version options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VersionStatus:
    out: VersionStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        out["options"] = data["Options"]
    else:
        raise DeserializationError("VersionStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("VersionStatus.status required")
    return out
