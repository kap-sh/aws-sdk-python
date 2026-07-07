"""Generated from Smithy shape ``com.amazonaws.swf#DomainDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_configuration
    import aws_sdk_swf.types.domain_info


class DomainDetail(TypedDict, closed=True):
    domain_info: "aws_sdk_swf.types.domain_info.DomainInfo"
    """<p>The basic information about a domain, such as its name, status, and description.</p>"""
    configuration: "aws_sdk_swf.types.domain_configuration.DomainConfiguration"
    """<p>The domain configuration. Currently, this includes only the domain's retention period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainDetail) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.domain_info

    out["domainInfo"] = aws_sdk_swf.types.domain_info.serialize_aws_json_1_0(
        value["domain_info"]
    )
    import aws_sdk_swf.types.domain_configuration

    out["configuration"] = (
        aws_sdk_swf.types.domain_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainDetail:
    out: DomainDetail = {}  # type: ignore[typeddict-item]
    if "domainInfo" in data:
        import aws_sdk_swf.types.domain_info

        out["domain_info"] = aws_sdk_swf.types.domain_info.deserialize_aws_json_1_0(
            data["domainInfo"]
        )
    else:
        raise DeserializationError("DomainDetail.domain_info required")
    if "configuration" in data:
        import aws_sdk_swf.types.domain_configuration

        out["configuration"] = (
            aws_sdk_swf.types.domain_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("DomainDetail.configuration required")
    return out
