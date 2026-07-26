"""Generated from Smithy shape ``com.amazonaws.iot#CreateBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_name
    import capo_iot.types.billing_group_properties
    import capo_iot.types.tag_list


class CreateBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: "capo_iot.types.billing_group_name.BillingGroupName"
    """<p>The name you wish to give to the billing group.</p>"""
    billing_group_properties: NotRequired[
        "capo_iot.types.billing_group_properties.BillingGroupProperties"
    ]
    """<p>The properties of the billing group.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillingGroupRequest) -> dict:
    out: dict = {}
    if "billing_group_properties" in value:
        import capo_iot.types.billing_group_properties

        out["billingGroupProperties"] = (
            capo_iot.types.billing_group_properties.serialize_json(
                value["billing_group_properties"]
            )
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBillingGroupRequest:
    out: CreateBillingGroupRequest = {}  # type: ignore[typeddict-item]
    if "billingGroupProperties" in data:
        import capo_iot.types.billing_group_properties

        out["billing_group_properties"] = (
            capo_iot.types.billing_group_properties.deserialize_json(
                data["billingGroupProperties"]
            )
        )
    if "tags" in data:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
