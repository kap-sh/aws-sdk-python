"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.campaign_name
    import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.update_campaign_action


class UpdateCampaignRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.campaign_name.campaignName"
    """<p> The name of the campaign to update. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>The description of the campaign.</p>"""
    data_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
    ]
    """<p> A list of vehicle attributes to associate with a signal. </p> <p>Default: An empty array</p>"""
    action: "aws_sdk_iotfleetwise.types.update_campaign_action.UpdateCampaignAction"
    """<p> Specifies how to update a campaign. The action can be one of the following:</p> <ul> <li> <p> <code>APPROVE</code> - To approve delivering a data collection scheme to vehicles. </p> </li> <li> <p> <code>SUSPEND</code> - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data.</p> </li> <li> <p> <code>RESUME</code> - To reactivate the <code>SUSPEND</code> campaign. The campaign is redeployed to all vehicles and the vehicles will resume sending data.</p> </li> <li> <p> <code>UPDATE</code> - To update a campaign. </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCampaignRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "data_extra_dimensions" in value:
        import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    import aws_sdk_iotfleetwise.types.update_campaign_action

    out["action"] = (
        aws_sdk_iotfleetwise.types.update_campaign_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCampaignRequest:
    out: UpdateCampaignRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "dataExtraDimensions" in data:
        import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if "action" in data:
        import aws_sdk_iotfleetwise.types.update_campaign_action

        out["action"] = (
            aws_sdk_iotfleetwise.types.update_campaign_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        raise DeserializationError("UpdateCampaignRequest.action required")
    return out
