"""Generated from Smithy shape ``com.amazonaws.opensearch#Limits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.additional_limit_list
    import capo_opensearch.types.instance_limits
    import capo_opensearch.types.storage_type_list


class Limits(TypedDict, closed=True):
    storage_types: NotRequired[
        "capo_opensearch.types.storage_type_list.StorageTypeList"
    ]
    """<p>Storage-related attributes that are available for a given instance type.</p>"""
    instance_limits: NotRequired["capo_opensearch.types.instance_limits.InstanceLimits"]
    """<p>The limits for a given instance type.</p>"""
    additional_limits: NotRequired[
        "capo_opensearch.types.additional_limit_list.AdditionalLimitList"
    ]
    """<p>List of additional limits that are specific to a given instance type for each of its instance roles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Limits) -> dict:
    out: dict = {}
    if "storage_types" in value:
        import capo_opensearch.types.storage_type_list

        out["StorageTypes"] = capo_opensearch.types.storage_type_list.serialize_json(
            value["storage_types"]
        )
    if "instance_limits" in value:
        import capo_opensearch.types.instance_limits

        out["InstanceLimits"] = capo_opensearch.types.instance_limits.serialize_json(
            value["instance_limits"]
        )
    if "additional_limits" in value:
        import capo_opensearch.types.additional_limit_list

        out["AdditionalLimits"] = (
            capo_opensearch.types.additional_limit_list.serialize_json(
                value["additional_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> Limits:
    out: Limits = {}  # type: ignore[typeddict-item]
    if "StorageTypes" in data:
        import capo_opensearch.types.storage_type_list

        out["storage_types"] = capo_opensearch.types.storage_type_list.deserialize_json(
            data["StorageTypes"]
        )
    if "InstanceLimits" in data:
        import capo_opensearch.types.instance_limits

        out["instance_limits"] = capo_opensearch.types.instance_limits.deserialize_json(
            data["InstanceLimits"]
        )
    if "AdditionalLimits" in data:
        import capo_opensearch.types.additional_limit_list

        out["additional_limits"] = (
            capo_opensearch.types.additional_limit_list.deserialize_json(
                data["AdditionalLimits"]
            )
        )
    return out
