"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.custom_log_source_attributes
    import aws_sdk_securitylake.types.custom_log_source_name
    import aws_sdk_securitylake.types.custom_log_source_provider
    import aws_sdk_securitylake.types.custom_log_source_version


class CustomLogSourceResource(TypedDict, closed=True):
    source_name: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_name.CustomLogSourceName"
    ]
    """<p>The name for a third-party custom source. This must be a Regionally unique value.</p>"""
    source_version: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
    ]
    """<p>The version for a third-party custom source. This must be a Regionally unique value.</p>"""
    provider: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_provider.CustomLogSourceProvider"
    ]
    """<p>The details of the log provider for a third-party custom source.</p>"""
    attributes: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_attributes.CustomLogSourceAttributes"
    ]
    """<p>The attributes of a third-party custom source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceResource) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "provider" in value:
        import aws_sdk_securitylake.types.custom_log_source_provider

        out["provider"] = (
            aws_sdk_securitylake.types.custom_log_source_provider.serialize_json(
                value["provider"]
            )
        )
    if "attributes" in value:
        import aws_sdk_securitylake.types.custom_log_source_attributes

        out["attributes"] = (
            aws_sdk_securitylake.types.custom_log_source_attributes.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLogSourceResource:
    out: CustomLogSourceResource = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "provider" in data:
        import aws_sdk_securitylake.types.custom_log_source_provider

        out["provider"] = (
            aws_sdk_securitylake.types.custom_log_source_provider.deserialize_json(
                data["provider"]
            )
        )
    if "attributes" in data:
        import aws_sdk_securitylake.types.custom_log_source_attributes

        out["attributes"] = (
            aws_sdk_securitylake.types.custom_log_source_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out
