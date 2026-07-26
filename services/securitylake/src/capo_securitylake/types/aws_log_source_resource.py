"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.aws_log_source_name
    import capo_securitylake.types.aws_log_source_version


class AwsLogSourceResource(TypedDict, closed=True):
    source_name: NotRequired[
        "capo_securitylake.types.aws_log_source_name.AwsLogSourceName"
    ]
    """<p>The name for a Amazon Web Services source. This must be a Regionally unique value.</p>"""
    source_version: NotRequired[
        "capo_securitylake.types.aws_log_source_version.AwsLogSourceVersion"
    ]
    """<p>The version for a Amazon Web Services source. This must be a Regionally unique value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceResource) -> dict:
    out: dict = {}
    if "source_name" in value:
        import capo_securitylake.types.aws_log_source_name

        out["sourceName"] = capo_securitylake.types.aws_log_source_name.serialize_json(
            value["source_name"]
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    return out


def deserialize_json(data: dict) -> AwsLogSourceResource:
    out: AwsLogSourceResource = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        import capo_securitylake.types.aws_log_source_name

        out["source_name"] = (
            capo_securitylake.types.aws_log_source_name.deserialize_json(
                data["sourceName"]
            )
        )
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    return out
