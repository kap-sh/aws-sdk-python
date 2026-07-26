"""Generated from Smithy shape ``com.amazonaws.iot#UpdateBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.billing_group_name
    import capo_iot.types.billing_group_properties
    import capo_iot.types.optional_version


class UpdateBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: "capo_iot.types.billing_group_name.BillingGroupName"
    """<p>The name of the billing group.</p>"""
    billing_group_properties: (
        "capo_iot.types.billing_group_properties.BillingGroupProperties"
    )
    """<p>The properties of the billing group.</p>"""
    expected_version: NotRequired["capo_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the <code>UpdateBillingGroup</code> request is rejected with a <code>VersionConflictException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupRequest) -> dict:
    out: dict = {}
    import capo_iot.types.billing_group_properties

    out["billingGroupProperties"] = (
        capo_iot.types.billing_group_properties.serialize_json(
            value["billing_group_properties"]
        )
    )
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupRequest:
    out: UpdateBillingGroupRequest = {}  # type: ignore[typeddict-item]
    if "billingGroupProperties" in data:
        import capo_iot.types.billing_group_properties

        out["billing_group_properties"] = (
            capo_iot.types.billing_group_properties.deserialize_json(
                data["billingGroupProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBillingGroupRequest.billing_group_properties required"
        )
    if "expectedVersion" in data:
        out["expected_version"] = data["expectedVersion"]
    return out
