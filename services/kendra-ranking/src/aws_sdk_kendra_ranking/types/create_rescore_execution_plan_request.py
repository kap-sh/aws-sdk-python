"""Generated from Smithy shape ``com.amazonaws.kendraranking#CreateRescoreExecutionPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.capacity_units_configuration
    import aws_sdk_kendra_ranking.types.client_token_name
    import aws_sdk_kendra_ranking.types.description
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_name
    import aws_sdk_kendra_ranking.types.tag_list


class CreateRescoreExecutionPlanRequest(TypedDict, closed=True):
    name: "aws_sdk_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
    """<p>A name for the rescore execution plan.</p>"""
    description: NotRequired["aws_sdk_kendra_ranking.types.description.Description"]
    """<p>A description for the rescore execution plan.</p>"""
    capacity_units: NotRequired[
        "aws_sdk_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    r"""<p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html\">Adjusting capacity</a>.</p>"""
    tags: NotRequired["aws_sdk_kendra_ranking.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired[
        "aws_sdk_kendra_ranking.types.client_token_name.ClientTokenName"
    ]
    """<p>A token that you provide to identify the request to create a rescore execution plan. Multiple calls to the <code>CreateRescoreExecutionPlanRequest</code> API with the same client token will create only one rescore execution plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRescoreExecutionPlanRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "capacity_units" in value:
        import aws_sdk_kendra_ranking.types.capacity_units_configuration

        out["CapacityUnits"] = (
            aws_sdk_kendra_ranking.types.capacity_units_configuration.serialize_aws_json_1_0(
                value["capacity_units"]
            )
        )
    if "tags" in value:
        import aws_sdk_kendra_ranking.types.tag_list

        out["Tags"] = aws_sdk_kendra_ranking.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRescoreExecutionPlanRequest:
    out: CreateRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRescoreExecutionPlanRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CapacityUnits" in data:
        import aws_sdk_kendra_ranking.types.capacity_units_configuration

        out["capacity_units"] = (
            aws_sdk_kendra_ranking.types.capacity_units_configuration.deserialize_aws_json_1_0(
                data["CapacityUnits"]
            )
        )
    if "Tags" in data:
        import aws_sdk_kendra_ranking.types.tag_list

        out["tags"] = aws_sdk_kendra_ranking.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
