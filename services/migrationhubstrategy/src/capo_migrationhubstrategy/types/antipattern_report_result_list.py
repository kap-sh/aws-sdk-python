"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AntipatternReportResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.antipattern_report_result

AntipatternReportResultList: TypeAlias = list[
    "capo_migrationhubstrategy.types.antipattern_report_result.AntipatternReportResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AntipatternReportResultList) -> list:
    import capo_migrationhubstrategy.types.antipattern_report_result

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.antipattern_report_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AntipatternReportResultList:
    import capo_migrationhubstrategy.types.antipattern_report_result

    out: AntipatternReportResultList = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.antipattern_report_result.deserialize_json(
                item
            )
        )
    return out
