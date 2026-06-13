"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFlowsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_name
    import aws_sdk_quicksight.types.search_filter_operator


class SearchFlowsFilter(TypedDict):
    name: "aws_sdk_quicksight.types.field_name.FieldName"
    """<p>The name of the value that you want to use as a filter, for example <code>\"Name\": \"DIRECT_QUICKSIGHT_SOLE_OWNER\"</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>assetName</code>: Any flows whose names have a substring match to this value will be returned.</p> </li> <li> <p> <code>assetDescription</code>: Any flows whose descriptions have a substring match to this value will be returned.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code>: Provide an ARN of a user or group, and any analyses with that ARN listed as the only owner of the analysis are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_OWNER</code>: Provide an ARN of a user or group, and any analyses with that ARN listed as one of the owners of the analyses are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_VIEWER_OR_OWNER</code>: Provide an ARN of a user or group, and any analyses with that ARN listed as one of the owners or viewers of the analyses are returned. Implicit permissions from folders or groups are not considered. </p> </li> </ul>"""
    operator: "aws_sdk_quicksight.types.search_filter_operator.SearchFilterOperator"
    """<p>The comparison operator that you want to use as a filter, for example <code>\"Operator\": \"StringEquals\"</code>. Valid values are <code>\"StringEquals\"</code> and <code>\"StringLike\"</code>.</p>"""
    value: "str"
    """<p>The value of the named item, in this case <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code>, that you want to use as a filter, for example <code>\"Value\"</code>. An example is <code>\"arn:aws:quicksight:us-east-1:1:user/default/UserName1\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFlowsFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.field_name

    out["Name"] = aws_sdk_quicksight.types.field_name.serialize_json(value["name"])
    import aws_sdk_quicksight.types.search_filter_operator

    out["Operator"] = aws_sdk_quicksight.types.search_filter_operator.serialize_json(
        value["operator"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SearchFlowsFilter:
    out: SearchFlowsFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_quicksight.types.field_name

        out["name"] = aws_sdk_quicksight.types.field_name.deserialize_json(data["Name"])
    else:
        raise DeserializationError("SearchFlowsFilter.name required")
    if "Operator" in data:
        import aws_sdk_quicksight.types.search_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.search_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("SearchFlowsFilter.operator required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("SearchFlowsFilter.value required")
    return out
