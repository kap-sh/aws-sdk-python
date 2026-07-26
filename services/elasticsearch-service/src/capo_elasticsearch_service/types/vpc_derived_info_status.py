"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VPCDerivedInfoStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.option_status
    import capo_elasticsearch_service.types.vpc_derived_info


class VPCDerivedInfoStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.vpc_derived_info.VPCDerivedInfo"
    """<p> Specifies the VPC options for the specified Elasticsearch domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the VPC options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCDerivedInfoStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.vpc_derived_info

    out["Options"] = capo_elasticsearch_service.types.vpc_derived_info.serialize_json(
        value["options"]
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VPCDerivedInfoStatus:
    out: VPCDerivedInfoStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_elasticsearch_service.types.vpc_derived_info

        out["options"] = (
            capo_elasticsearch_service.types.vpc_derived_info.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("VPCDerivedInfoStatus.options required")
    if "Status" in data:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("VPCDerivedInfoStatus.status required")
    return out
