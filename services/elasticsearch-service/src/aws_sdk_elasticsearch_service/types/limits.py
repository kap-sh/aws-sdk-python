"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#Limits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.additional_limit_list
    import aws_sdk_elasticsearch_service.types.instance_limits
    import aws_sdk_elasticsearch_service.types.storage_type_list


class Limits(TypedDict, closed=True):
    storage_types: NotRequired[
        "aws_sdk_elasticsearch_service.types.storage_type_list.StorageTypeList"
    ]
    """<p>StorageType represents the list of storage related types and attributes that are available for given InstanceType. </p>"""
    instance_limits: NotRequired[
        "aws_sdk_elasticsearch_service.types.instance_limits.InstanceLimits"
    ]
    additional_limits: NotRequired[
        "aws_sdk_elasticsearch_service.types.additional_limit_list.AdditionalLimitList"
    ]
    """<p> List of additional limits that are specific to a given InstanceType and for each of it's <code> <a>InstanceRole</a> </code> . </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Limits) -> dict:
    out: dict = {}
    if "storage_types" in value:
        import aws_sdk_elasticsearch_service.types.storage_type_list

        out["StorageTypes"] = (
            aws_sdk_elasticsearch_service.types.storage_type_list.serialize_json(
                value["storage_types"]
            )
        )
    if "instance_limits" in value:
        import aws_sdk_elasticsearch_service.types.instance_limits

        out["InstanceLimits"] = (
            aws_sdk_elasticsearch_service.types.instance_limits.serialize_json(
                value["instance_limits"]
            )
        )
    if "additional_limits" in value:
        import aws_sdk_elasticsearch_service.types.additional_limit_list

        out["AdditionalLimits"] = (
            aws_sdk_elasticsearch_service.types.additional_limit_list.serialize_json(
                value["additional_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> Limits:
    out: Limits = {}  # type: ignore[typeddict-item]
    if "StorageTypes" in data:
        import aws_sdk_elasticsearch_service.types.storage_type_list

        out["storage_types"] = (
            aws_sdk_elasticsearch_service.types.storage_type_list.deserialize_json(
                data["StorageTypes"]
            )
        )
    if "InstanceLimits" in data:
        import aws_sdk_elasticsearch_service.types.instance_limits

        out["instance_limits"] = (
            aws_sdk_elasticsearch_service.types.instance_limits.deserialize_json(
                data["InstanceLimits"]
            )
        )
    if "AdditionalLimits" in data:
        import aws_sdk_elasticsearch_service.types.additional_limit_list

        out["additional_limits"] = (
            aws_sdk_elasticsearch_service.types.additional_limit_list.deserialize_json(
                data["AdditionalLimits"]
            )
        )
    return out
