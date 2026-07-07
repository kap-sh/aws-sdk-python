"""Generated from Smithy shape ``com.amazonaws.dlm#GetLifecyclePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.default_policies_type_values
    import aws_sdk_dlm.types.gettable_policy_state_values
    import aws_sdk_dlm.types.policy_id_list
    import aws_sdk_dlm.types.resource_type_values_list
    import aws_sdk_dlm.types.tags_to_add_filter_list
    import aws_sdk_dlm.types.target_tags_filter_list


class GetLifecyclePoliciesRequest(TypedDict, closed=True):
    policy_ids: NotRequired["aws_sdk_dlm.types.policy_id_list.PolicyIdList"]
    """<p>The identifiers of the data lifecycle policies.</p>"""
    state: NotRequired[
        "aws_sdk_dlm.types.gettable_policy_state_values.GettablePolicyStateValues"
    ]
    """<p>The activation state.</p>"""
    resource_types: NotRequired[
        "aws_sdk_dlm.types.resource_type_values_list.ResourceTypeValuesList"
    ]
    """<p>The resource type.</p>"""
    target_tags: NotRequired[
        "aws_sdk_dlm.types.target_tags_filter_list.TargetTagsFilterList"
    ]
    """<p>The target tag for a policy.</p> <p>Tags are strings in the format <code>key=value</code>.</p>"""
    tags_to_add: NotRequired[
        "aws_sdk_dlm.types.tags_to_add_filter_list.TagsToAddFilterList"
    ]
    """<p>The tags to add to objects created by the policy.</p> <p>Tags are strings in the format <code>key=value</code>.</p> <p>These user-defined tags are added in addition to the Amazon Web Services-added lifecycle tags.</p>"""
    default_policy_type: NotRequired[
        "aws_sdk_dlm.types.default_policies_type_values.DefaultPoliciesTypeValues"
    ]
    """<p> <b>[Default policies only]</b> Specifies the type of default policy to get. Specify one of the following:</p> <ul> <li> <p> <code>VOLUME</code> - To get only the default policy for EBS snapshots</p> </li> <li> <p> <code>INSTANCE</code> - To get only the default policy for EBS-backed AMIs</p> </li> <li> <p> <code>ALL</code> - To get all default policies</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLifecyclePoliciesRequest:
    out: GetLifecyclePoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
