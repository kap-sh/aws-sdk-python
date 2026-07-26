"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.datasource_package_ingest_state
    import capo_detective.types.last_ingest_state_change_dates


class DatasourcePackageIngestDetail(TypedDict, closed=True):
    datasource_package_ingest_state: NotRequired[
        "capo_detective.types.datasource_package_ingest_state.DatasourcePackageIngestState"
    ]
    """<p>Details on which data source packages are ingested for a member account.</p>"""
    last_ingest_state_change: NotRequired[
        "capo_detective.types.last_ingest_state_change_dates.LastIngestStateChangeDates"
    ]
    """<p>The date a data source package was enabled for this account</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackageIngestDetail) -> dict:
    out: dict = {}
    if "datasource_package_ingest_state" in value:
        import capo_detective.types.datasource_package_ingest_state

        out["DatasourcePackageIngestState"] = (
            capo_detective.types.datasource_package_ingest_state.serialize_json(
                value["datasource_package_ingest_state"]
            )
        )
    if "last_ingest_state_change" in value:
        import capo_detective.types.last_ingest_state_change_dates

        out["LastIngestStateChange"] = (
            capo_detective.types.last_ingest_state_change_dates.serialize_json(
                value["last_ingest_state_change"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageIngestDetail:
    out: DatasourcePackageIngestDetail = {}  # type: ignore[typeddict-item]
    if "DatasourcePackageIngestState" in data:
        import capo_detective.types.datasource_package_ingest_state

        out["datasource_package_ingest_state"] = (
            capo_detective.types.datasource_package_ingest_state.deserialize_json(
                data["DatasourcePackageIngestState"]
            )
        )
    if "LastIngestStateChange" in data:
        import capo_detective.types.last_ingest_state_change_dates

        out["last_ingest_state_change"] = (
            capo_detective.types.last_ingest_state_change_dates.deserialize_json(
                data["LastIngestStateChange"]
            )
        )
    return out
