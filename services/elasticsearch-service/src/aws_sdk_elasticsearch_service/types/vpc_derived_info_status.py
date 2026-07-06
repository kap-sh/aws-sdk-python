"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VPCDerivedInfoStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.option_status
    import aws_sdk_elasticsearch_service.types.vpc_derived_info


class VPCDerivedInfoStatus(TypedDict, closed=True):
    options: "aws_sdk_elasticsearch_service.types.vpc_derived_info.VPCDerivedInfo"
    """<p> Specifies the VPC options for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the VPC options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCDerivedInfoStatus) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.vpc_derived_info

    out["Options"] = (
        aws_sdk_elasticsearch_service.types.vpc_derived_info.serialize_json(
            value["options"]
        )
    )
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VPCDerivedInfoStatus:
    out: VPCDerivedInfoStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_elasticsearch_service.types.vpc_derived_info

        out["options"] = (
            aws_sdk_elasticsearch_service.types.vpc_derived_info.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("VPCDerivedInfoStatus.options required")
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("VPCDerivedInfoStatus.status required")
    return out
