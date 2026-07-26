"""Generated from Smithy shape ``com.amazonaws.databrew#FormatOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.csv_options
    import capo_databrew.types.excel_options
    import capo_databrew.types.json_options


class FormatOptions(TypedDict, closed=True):
    json: NotRequired["capo_databrew.types.json_options.JsonOptions"]
    """<p>Options that define how JSON input is to be interpreted by DataBrew.</p>"""
    excel: NotRequired["capo_databrew.types.excel_options.ExcelOptions"]
    """<p>Options that define how Excel input is to be interpreted by DataBrew.</p>"""
    csv: NotRequired["capo_databrew.types.csv_options.CsvOptions"]
    """<p>Options that define how CSV input is to be interpreted by DataBrew.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormatOptions) -> dict:
    out: dict = {}
    if "json" in value:
        import capo_databrew.types.json_options

        out["Json"] = capo_databrew.types.json_options.serialize_json(value["json"])
    if "excel" in value:
        import capo_databrew.types.excel_options

        out["Excel"] = capo_databrew.types.excel_options.serialize_json(value["excel"])
    if "csv" in value:
        import capo_databrew.types.csv_options

        out["Csv"] = capo_databrew.types.csv_options.serialize_json(value["csv"])
    return out


def deserialize_json(data: dict) -> FormatOptions:
    out: FormatOptions = {}  # type: ignore[typeddict-item]
    if "Json" in data:
        import capo_databrew.types.json_options

        out["json"] = capo_databrew.types.json_options.deserialize_json(data["Json"])
    if "Excel" in data:
        import capo_databrew.types.excel_options

        out["excel"] = capo_databrew.types.excel_options.deserialize_json(data["Excel"])
    if "Csv" in data:
        import capo_databrew.types.csv_options

        out["csv"] = capo_databrew.types.csv_options.deserialize_json(data["Csv"])
    return out
