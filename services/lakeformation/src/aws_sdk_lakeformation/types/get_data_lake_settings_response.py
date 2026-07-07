"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetDataLakeSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_lake_settings


class GetDataLakeSettingsResponse(TypedDict, closed=True):
    data_lake_settings: NotRequired[
        "aws_sdk_lakeformation.types.data_lake_settings.DataLakeSettings"
    ]
    """<p>A structure representing a list of Lake Formation principals designated as data lake administrators.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeSettingsResponse) -> dict:
    out: dict = {}
    if "data_lake_settings" in value:
        import aws_sdk_lakeformation.types.data_lake_settings

        out["DataLakeSettings"] = (
            aws_sdk_lakeformation.types.data_lake_settings.serialize_json(
                value["data_lake_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataLakeSettingsResponse:
    out: GetDataLakeSettingsResponse = {}  # type: ignore[typeddict-item]
    if "DataLakeSettings" in data:
        import aws_sdk_lakeformation.types.data_lake_settings

        out["data_lake_settings"] = (
            aws_sdk_lakeformation.types.data_lake_settings.deserialize_json(
                data["DataLakeSettings"]
            )
        )
    return out
