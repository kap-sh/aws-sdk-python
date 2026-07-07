"""Generated from Smithy shape ``com.amazonaws.iot#DeleteBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.optional_version


class DeleteBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    """<p>The name of the billing group.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the <code>DeleteBillingGroup</code> request is rejected with a <code>VersionConflictException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBillingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBillingGroupRequest:
    out: DeleteBillingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
