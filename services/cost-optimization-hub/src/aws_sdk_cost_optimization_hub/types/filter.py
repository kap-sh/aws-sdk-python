"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.account_id_list
    import aws_sdk_cost_optimization_hub.types.action_type_list
    import aws_sdk_cost_optimization_hub.types.implementation_effort_list
    import aws_sdk_cost_optimization_hub.types.recommendation_id_list
    import aws_sdk_cost_optimization_hub.types.region_list
    import aws_sdk_cost_optimization_hub.types.resource_arn_list
    import aws_sdk_cost_optimization_hub.types.resource_id_list
    import aws_sdk_cost_optimization_hub.types.resource_type_list
    import aws_sdk_cost_optimization_hub.types.tag_list


class Filter(TypedDict):
    restart_needed: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation requires a restart.</p>"""
    rollback_possible: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation can be rolled back.</p>"""
    implementation_efforts: NotRequired[
        "aws_sdk_cost_optimization_hub.types.implementation_effort_list.ImplementationEffortList"
    ]
    """<p>The effort required to implement the recommendation.</p>"""
    account_ids: NotRequired[
        "aws_sdk_cost_optimization_hub.types.account_id_list.AccountIdList"
    ]
    """<p>The account to which the recommendation applies.</p>"""
    regions: NotRequired["aws_sdk_cost_optimization_hub.types.region_list.RegionList"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_types: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_type_list.ResourceTypeList"
    ]
    """<p>The resource type of the recommendation.</p>"""
    action_types: NotRequired[
        "aws_sdk_cost_optimization_hub.types.action_type_list.ActionTypeList"
    ]
    """<p>The type of action you can take by adopting the recommendation.</p>"""
    tags: NotRequired["aws_sdk_cost_optimization_hub.types.tag_list.TagList"]
    """<p>A list of tags assigned to the recommendation.</p>"""
    resource_ids: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_id_list.ResourceIdList"
    ]
    """<p>The resource ID of the recommendation.</p>"""
    resource_arns: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_arn_list.ResourceArnList"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation.</p>"""
    recommendation_ids: NotRequired[
        "aws_sdk_cost_optimization_hub.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>The IDs for the recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filter) -> dict:
    out: dict = {}
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "rollback_possible" in value:
        out["rollbackPossible"] = value["rollback_possible"]
    if "implementation_efforts" in value:
        import aws_sdk_cost_optimization_hub.types.implementation_effort_list

        out["implementationEfforts"] = (
            aws_sdk_cost_optimization_hub.types.implementation_effort_list.serialize_aws_json_1_0(
                value["implementation_efforts"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_cost_optimization_hub.types.account_id_list

        out["accountIds"] = (
            aws_sdk_cost_optimization_hub.types.account_id_list.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "regions" in value:
        import aws_sdk_cost_optimization_hub.types.region_list

        out["regions"] = (
            aws_sdk_cost_optimization_hub.types.region_list.serialize_aws_json_1_0(
                value["regions"]
            )
        )
    if "resource_types" in value:
        import aws_sdk_cost_optimization_hub.types.resource_type_list

        out["resourceTypes"] = (
            aws_sdk_cost_optimization_hub.types.resource_type_list.serialize_aws_json_1_0(
                value["resource_types"]
            )
        )
    if "action_types" in value:
        import aws_sdk_cost_optimization_hub.types.action_type_list

        out["actionTypes"] = (
            aws_sdk_cost_optimization_hub.types.action_type_list.serialize_aws_json_1_0(
                value["action_types"]
            )
        )
    if "tags" in value:
        import aws_sdk_cost_optimization_hub.types.tag_list

        out["tags"] = (
            aws_sdk_cost_optimization_hub.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "resource_ids" in value:
        import aws_sdk_cost_optimization_hub.types.resource_id_list

        out["resourceIds"] = (
            aws_sdk_cost_optimization_hub.types.resource_id_list.serialize_aws_json_1_0(
                value["resource_ids"]
            )
        )
    if "resource_arns" in value:
        import aws_sdk_cost_optimization_hub.types.resource_arn_list

        out["resourceArns"] = (
            aws_sdk_cost_optimization_hub.types.resource_arn_list.serialize_aws_json_1_0(
                value["resource_arns"]
            )
        )
    if "recommendation_ids" in value:
        import aws_sdk_cost_optimization_hub.types.recommendation_id_list

        out["recommendationIds"] = (
            aws_sdk_cost_optimization_hub.types.recommendation_id_list.serialize_aws_json_1_0(
                value["recommendation_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "restartNeeded" in data:
        out["restart_needed"] = data["restartNeeded"]
    if "rollbackPossible" in data:
        out["rollback_possible"] = data["rollbackPossible"]
    if "implementationEfforts" in data:
        import aws_sdk_cost_optimization_hub.types.implementation_effort_list

        out["implementation_efforts"] = (
            aws_sdk_cost_optimization_hub.types.implementation_effort_list.deserialize_aws_json_1_0(
                data["implementationEfforts"]
            )
        )
    if "accountIds" in data:
        import aws_sdk_cost_optimization_hub.types.account_id_list

        out["account_ids"] = (
            aws_sdk_cost_optimization_hub.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "regions" in data:
        import aws_sdk_cost_optimization_hub.types.region_list

        out["regions"] = (
            aws_sdk_cost_optimization_hub.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    if "resourceTypes" in data:
        import aws_sdk_cost_optimization_hub.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_cost_optimization_hub.types.resource_type_list.deserialize_aws_json_1_0(
                data["resourceTypes"]
            )
        )
    if "actionTypes" in data:
        import aws_sdk_cost_optimization_hub.types.action_type_list

        out["action_types"] = (
            aws_sdk_cost_optimization_hub.types.action_type_list.deserialize_aws_json_1_0(
                data["actionTypes"]
            )
        )
    if "tags" in data:
        import aws_sdk_cost_optimization_hub.types.tag_list

        out["tags"] = (
            aws_sdk_cost_optimization_hub.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if "resourceIds" in data:
        import aws_sdk_cost_optimization_hub.types.resource_id_list

        out["resource_ids"] = (
            aws_sdk_cost_optimization_hub.types.resource_id_list.deserialize_aws_json_1_0(
                data["resourceIds"]
            )
        )
    if "resourceArns" in data:
        import aws_sdk_cost_optimization_hub.types.resource_arn_list

        out["resource_arns"] = (
            aws_sdk_cost_optimization_hub.types.resource_arn_list.deserialize_aws_json_1_0(
                data["resourceArns"]
            )
        )
    if "recommendationIds" in data:
        import aws_sdk_cost_optimization_hub.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_cost_optimization_hub.types.recommendation_id_list.deserialize_aws_json_1_0(
                data["recommendationIds"]
            )
        )
    return out
