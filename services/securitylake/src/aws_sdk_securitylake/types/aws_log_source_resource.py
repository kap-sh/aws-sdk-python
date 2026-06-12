"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceResource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_name
    import aws_sdk_securitylake.types.aws_log_source_version

class AwsLogSourceResource(TypedDict):
    source_name: NotRequired["aws_sdk_securitylake.types.aws_log_source_name.AwsLogSourceName"]
    """<p>The name for a Amazon Web Services source. This must be a Regionally unique value.</p>"""
    source_version: NotRequired["aws_sdk_securitylake.types.aws_log_source_version.AwsLogSourceVersion"]
    """<p>The version for a Amazon Web Services source. This must be a Regionally unique value.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceResource) -> dict:
    out: dict = {}
    if "source_name" in value:
        import aws_sdk_securitylake.types.aws_log_source_name
        out["sourceName"] = aws_sdk_securitylake.types.aws_log_source_name.serialize_json(value["source_name"])
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    return out


def deserialize_json(data: dict) -> AwsLogSourceResource:
    out: AwsLogSourceResource = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        import aws_sdk_securitylake.types.aws_log_source_name
        out["source_name"] = aws_sdk_securitylake.types.aws_log_source_name.deserialize_json(data["sourceName"])
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    return out