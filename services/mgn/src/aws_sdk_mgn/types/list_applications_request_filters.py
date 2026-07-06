"""Generated from Smithy shape ``com.amazonaws.mgn#ListApplicationsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application_i_ds_filter
    import aws_sdk_mgn.types.wave_i_ds_filter


class ListApplicationsRequestFilters(TypedDict, closed=True):
    application_i_ds: NotRequired[
        "aws_sdk_mgn.types.application_i_ds_filter.ApplicationIDsFilter"
    ]
    """<p>Filter applications list by application ID.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Filter applications list by archival status.</p>"""
    wave_i_ds: NotRequired["aws_sdk_mgn.types.wave_i_ds_filter.WaveIDsFilter"]
    """<p>Filter applications list by wave ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequestFilters) -> dict:
    out: dict = {}
    if "application_i_ds" in value:
        import aws_sdk_mgn.types.application_i_ds_filter

        out["applicationIDs"] = (
            aws_sdk_mgn.types.application_i_ds_filter.serialize_json(
                value["application_i_ds"]
            )
        )
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "wave_i_ds" in value:
        import aws_sdk_mgn.types.wave_i_ds_filter

        out["waveIDs"] = aws_sdk_mgn.types.wave_i_ds_filter.serialize_json(
            value["wave_i_ds"]
        )
    return out


def deserialize_json(data: dict) -> ListApplicationsRequestFilters:
    out: ListApplicationsRequestFilters = {}  # type: ignore[typeddict-item]
    if "applicationIDs" in data:
        import aws_sdk_mgn.types.application_i_ds_filter

        out["application_i_ds"] = (
            aws_sdk_mgn.types.application_i_ds_filter.deserialize_json(
                data["applicationIDs"]
            )
        )
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    if "waveIDs" in data:
        import aws_sdk_mgn.types.wave_i_ds_filter

        out["wave_i_ds"] = aws_sdk_mgn.types.wave_i_ds_filter.deserialize_json(
            data["waveIDs"]
        )
    return out
