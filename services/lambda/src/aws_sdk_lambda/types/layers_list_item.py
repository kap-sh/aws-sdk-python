"""Generated from Smithy shape ``com.amazonaws.lambda#LayersListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layer_arn
    import aws_sdk_lambda.types.layer_name
    import aws_sdk_lambda.types.layer_versions_list_item


class LayersListItem(TypedDict, closed=True):
    layer_name: NotRequired["aws_sdk_lambda.types.layer_name.LayerName"]
    """<p>The name of the layer.</p>"""
    layer_arn: NotRequired["aws_sdk_lambda.types.layer_arn.LayerArn"]
    """<p>The Amazon Resource Name (ARN) of the function layer.</p>"""
    latest_matching_version: NotRequired[
        "aws_sdk_lambda.types.layer_versions_list_item.LayerVersionsListItem"
    ]
    """<p>The newest version of the layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayersListItem) -> dict:
    out: dict = {}
    if "layer_name" in value:
        out["LayerName"] = value["layer_name"]
    if "layer_arn" in value:
        out["LayerArn"] = value["layer_arn"]
    if "latest_matching_version" in value:
        import aws_sdk_lambda.types.layer_versions_list_item

        out["LatestMatchingVersion"] = (
            aws_sdk_lambda.types.layer_versions_list_item.serialize_json(
                value["latest_matching_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> LayersListItem:
    out: LayersListItem = {}  # type: ignore[typeddict-item]
    if "LayerName" in data:
        out["layer_name"] = data["LayerName"]
    if "LayerArn" in data:
        out["layer_arn"] = data["LayerArn"]
    if "LatestMatchingVersion" in data:
        import aws_sdk_lambda.types.layer_versions_list_item

        out["latest_matching_version"] = (
            aws_sdk_lambda.types.layer_versions_list_item.deserialize_json(
                data["LatestMatchingVersion"]
            )
        )
    return out
