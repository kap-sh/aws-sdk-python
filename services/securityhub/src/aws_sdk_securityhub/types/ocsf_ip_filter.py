"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfIpFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ip_filter
    import aws_sdk_securityhub.types.ocsf_ip_field


class OcsfIpFilter(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_securityhub.types.ocsf_ip_field.OcsfIpField"]
    """<p>The name of the IP address field to filter on.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.ip_filter.IpFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfIpFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.ocsf_ip_field

        out["FieldName"] = aws_sdk_securityhub.types.ocsf_ip_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.ip_filter

        out["Filter"] = aws_sdk_securityhub.types.ip_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> OcsfIpFilter:
    out: OcsfIpFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.ocsf_ip_field

        out["field_name"] = aws_sdk_securityhub.types.ocsf_ip_field.deserialize_json(
            data["FieldName"]
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.ip_filter

        out["filter"] = aws_sdk_securityhub.types.ip_filter.deserialize_json(
            data["Filter"]
        )
    return out
