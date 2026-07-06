"""Generated from Smithy shape ``com.amazonaws.quicksight#PutDataSetRefreshPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.data_set_refresh_properties
    import aws_sdk_quicksight.types.resource_id


class PutDataSetRefreshPropertiesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset.</p>"""
    data_set_refresh_properties: (
        "aws_sdk_quicksight.types.data_set_refresh_properties.DataSetRefreshProperties"
    )
    """<p>The dataset refresh properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDataSetRefreshPropertiesRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_refresh_properties

    out["DataSetRefreshProperties"] = (
        aws_sdk_quicksight.types.data_set_refresh_properties.serialize_json(
            value["data_set_refresh_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutDataSetRefreshPropertiesRequest:
    out: PutDataSetRefreshPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "DataSetRefreshProperties" in data:
        import aws_sdk_quicksight.types.data_set_refresh_properties

        out["data_set_refresh_properties"] = (
            aws_sdk_quicksight.types.data_set_refresh_properties.deserialize_json(
                data["DataSetRefreshProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PutDataSetRefreshPropertiesRequest.data_set_refresh_properties required"
        )
    return out
