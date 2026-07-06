"""Generated from Smithy shape ``com.amazonaws.glue#CreateCsvClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.csv_column_delimiter
    import aws_sdk_glue.types.csv_header
    import aws_sdk_glue.types.csv_header_option
    import aws_sdk_glue.types.csv_quote_symbol
    import aws_sdk_glue.types.csv_serde_option
    import aws_sdk_glue.types.custom_datatypes
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_boolean


class CreateCsvClassifierRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    delimiter: NotRequired["aws_sdk_glue.types.csv_column_delimiter.CsvColumnDelimiter"]
    """<p>A custom symbol to denote what separates each column entry in the row.</p>"""
    quote_symbol: NotRequired["aws_sdk_glue.types.csv_quote_symbol.CsvQuoteSymbol"]
    """<p>A custom symbol to denote what combines content into a single column value. Must be different from the column delimiter.</p>"""
    contains_header: NotRequired["aws_sdk_glue.types.csv_header_option.CsvHeaderOption"]
    """<p>Indicates whether the CSV file contains a header.</p>"""
    header: NotRequired["aws_sdk_glue.types.csv_header.CsvHeader"]
    """<p>A list of strings representing column names.</p>"""
    disable_value_trimming: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies not to trim values before identifying the type of column values. The default value is true.</p>"""
    allow_single_column: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables the processing of files that contain only one column.</p>"""
    custom_datatype_configured: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables the configuration of custom datatypes.</p>"""
    custom_datatypes: NotRequired["aws_sdk_glue.types.custom_datatypes.CustomDatatypes"]
    """<p>Creates a list of supported custom datatypes.</p>"""
    serde: NotRequired["aws_sdk_glue.types.csv_serde_option.CsvSerdeOption"]
    """<p>Sets the SerDe for processing CSV in the classifier, which will be applied in the Data Catalog. Valid values are <code>OpenCSVSerDe</code>, <code>LazySimpleSerDe</code>, and <code>None</code>. You can specify the <code>None</code> value when you want the crawler to do the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCsvClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "quote_symbol" in value:
        out["QuoteSymbol"] = value["quote_symbol"]
    if "contains_header" in value:
        import aws_sdk_glue.types.csv_header_option

        out["ContainsHeader"] = (
            aws_sdk_glue.types.csv_header_option.serialize_aws_json_1_1(
                value["contains_header"]
            )
        )
    if "header" in value:
        import aws_sdk_glue.types.csv_header

        out["Header"] = aws_sdk_glue.types.csv_header.serialize_aws_json_1_1(
            value["header"]
        )
    if "disable_value_trimming" in value:
        out["DisableValueTrimming"] = value["disable_value_trimming"]
    if "allow_single_column" in value:
        out["AllowSingleColumn"] = value["allow_single_column"]
    if "custom_datatype_configured" in value:
        out["CustomDatatypeConfigured"] = value["custom_datatype_configured"]
    if "custom_datatypes" in value:
        import aws_sdk_glue.types.custom_datatypes

        out["CustomDatatypes"] = (
            aws_sdk_glue.types.custom_datatypes.serialize_aws_json_1_1(
                value["custom_datatypes"]
            )
        )
    if "serde" in value:
        import aws_sdk_glue.types.csv_serde_option

        out["Serde"] = aws_sdk_glue.types.csv_serde_option.serialize_aws_json_1_1(
            value["serde"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCsvClassifierRequest:
    out: CreateCsvClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCsvClassifierRequest.name required")
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "QuoteSymbol" in data:
        out["quote_symbol"] = data["QuoteSymbol"]
    if "ContainsHeader" in data:
        import aws_sdk_glue.types.csv_header_option

        out["contains_header"] = (
            aws_sdk_glue.types.csv_header_option.deserialize_aws_json_1_1(
                data["ContainsHeader"]
            )
        )
    if "Header" in data:
        import aws_sdk_glue.types.csv_header

        out["header"] = aws_sdk_glue.types.csv_header.deserialize_aws_json_1_1(
            data["Header"]
        )
    if "DisableValueTrimming" in data:
        out["disable_value_trimming"] = data["DisableValueTrimming"]
    if "AllowSingleColumn" in data:
        out["allow_single_column"] = data["AllowSingleColumn"]
    if "CustomDatatypeConfigured" in data:
        out["custom_datatype_configured"] = data["CustomDatatypeConfigured"]
    if "CustomDatatypes" in data:
        import aws_sdk_glue.types.custom_datatypes

        out["custom_datatypes"] = (
            aws_sdk_glue.types.custom_datatypes.deserialize_aws_json_1_1(
                data["CustomDatatypes"]
            )
        )
    if "Serde" in data:
        import aws_sdk_glue.types.csv_serde_option

        out["serde"] = aws_sdk_glue.types.csv_serde_option.deserialize_aws_json_1_1(
            data["Serde"]
        )
    return out
