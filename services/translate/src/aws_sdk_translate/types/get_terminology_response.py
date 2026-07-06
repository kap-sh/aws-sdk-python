"""Generated from Smithy shape ``com.amazonaws.translate#GetTerminologyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_translate.types.terminology_data_location
    import aws_sdk_translate.types.terminology_properties


class GetTerminologyResponse(TypedDict, closed=True):
    terminology_properties: NotRequired[
        "aws_sdk_translate.types.terminology_properties.TerminologyProperties"
    ]
    """<p>The properties of the custom terminology being retrieved.</p>"""
    terminology_data_location: NotRequired[
        "aws_sdk_translate.types.terminology_data_location.TerminologyDataLocation"
    ]
    """<p>The Amazon S3 location of the most recent custom terminology input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration.</p> <important> <p>Amazon Translate doesn't scan all input files for the risk of CSV injection attacks. </p> <p>CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.</p> <p>Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.</p> </important>"""
    auxiliary_data_location: NotRequired[
        "aws_sdk_translate.types.terminology_data_location.TerminologyDataLocation"
    ]
    """<p>The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a terminology resource. The location is returned as a presigned URL to that has a 30-minute expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTerminologyResponse) -> dict:
    out: dict = {}
    if "terminology_properties" in value:
        import aws_sdk_translate.types.terminology_properties

        out["TerminologyProperties"] = (
            aws_sdk_translate.types.terminology_properties.serialize_aws_json_1_1(
                value["terminology_properties"]
            )
        )
    if "terminology_data_location" in value:
        import aws_sdk_translate.types.terminology_data_location

        out["TerminologyDataLocation"] = (
            aws_sdk_translate.types.terminology_data_location.serialize_aws_json_1_1(
                value["terminology_data_location"]
            )
        )
    if "auxiliary_data_location" in value:
        import aws_sdk_translate.types.terminology_data_location

        out["AuxiliaryDataLocation"] = (
            aws_sdk_translate.types.terminology_data_location.serialize_aws_json_1_1(
                value["auxiliary_data_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTerminologyResponse:
    out: GetTerminologyResponse = {}  # type: ignore[typeddict-item]
    if "TerminologyProperties" in data:
        import aws_sdk_translate.types.terminology_properties

        out["terminology_properties"] = (
            aws_sdk_translate.types.terminology_properties.deserialize_aws_json_1_1(
                data["TerminologyProperties"]
            )
        )
    if "TerminologyDataLocation" in data:
        import aws_sdk_translate.types.terminology_data_location

        out["terminology_data_location"] = (
            aws_sdk_translate.types.terminology_data_location.deserialize_aws_json_1_1(
                data["TerminologyDataLocation"]
            )
        )
    if "AuxiliaryDataLocation" in data:
        import aws_sdk_translate.types.terminology_data_location

        out["auxiliary_data_location"] = (
            aws_sdk_translate.types.terminology_data_location.deserialize_aws_json_1_1(
                data["AuxiliaryDataLocation"]
            )
        )
    return out
