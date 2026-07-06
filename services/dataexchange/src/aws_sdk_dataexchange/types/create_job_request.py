"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.asset_configuration
    import aws_sdk_dataexchange.types.request_details
    import aws_sdk_dataexchange.types.type


class CreateJobRequest(TypedDict, closed=True):
    asset_configuration: NotRequired[
        "aws_sdk_dataexchange.types.asset_configuration.AssetConfiguration"
    ]
    """<p>The configuration for the asset, including tags to be applied to assets created by the job.</p>"""
    details: "aws_sdk_dataexchange.types.request_details.RequestDetails"
    """<p>The details for the CreateJob request.</p>"""
    type: "aws_sdk_dataexchange.types.type.Type"
    """<p>The type of job to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "asset_configuration" in value:
        import aws_sdk_dataexchange.types.asset_configuration

        out["AssetConfiguration"] = (
            aws_sdk_dataexchange.types.asset_configuration.serialize_json(
                value["asset_configuration"]
            )
        )
    import aws_sdk_dataexchange.types.request_details

    out["Details"] = aws_sdk_dataexchange.types.request_details.serialize_json(
        value["details"]
    )
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if "AssetConfiguration" in data:
        import aws_sdk_dataexchange.types.asset_configuration

        out["asset_configuration"] = (
            aws_sdk_dataexchange.types.asset_configuration.deserialize_json(
                data["AssetConfiguration"]
            )
        )
    if "Details" in data:
        import aws_sdk_dataexchange.types.request_details

        out["details"] = aws_sdk_dataexchange.types.request_details.deserialize_json(
            data["Details"]
        )
    else:
        raise DeserializationError("CreateJobRequest.details required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("CreateJobRequest.type required")
    return out
