"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.directionality
    import aws_sdk_translate.types.terminology_data_format
    import aws_sdk_translate.types.terminology_file


class TerminologyData(TypedDict, closed=True):
    file: "aws_sdk_translate.types.terminology_file.TerminologyFile"
    """<p>The file containing the custom terminology data. Your version of the AWS SDK performs a Base64-encoding on this field before sending a request to the AWS service. Users of the SDK should not perform Base64-encoding themselves.</p>"""
    format: "aws_sdk_translate.types.terminology_data_format.TerminologyDataFormat"
    """<p>The data format of the custom terminology.</p>"""
    directionality: NotRequired["aws_sdk_translate.types.directionality.Directionality"]
    """<p>The directionality of your terminology resource indicates whether it has one source language (uni-directional) or multiple (multi-directional).</p> <dl> <dt>UNI</dt> <dd> <p>The terminology resource has one source language (for example, the first column in a CSV file), and all of its other languages are target languages. </p> </dd> <dt>MULTI</dt> <dd> <p>Any language in the terminology resource can be the source language or a target language. A single multi-directional terminology resource can be used for jobs that translate different language pairs. For example, if the terminology contains English and Spanish terms, it can be used for jobs that translate English to Spanish and Spanish to English.</p> </dd> </dl> <p>When you create a custom terminology resource without specifying the directionality, it behaves as uni-directional terminology, although this parameter will have a null value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyData) -> dict:
    out: dict = {}
    import aws_sdk_translate.types.terminology_file

    out["File"] = aws_sdk_translate.types.terminology_file.serialize_aws_json_1_1(
        value["file"]
    )
    import aws_sdk_translate.types.terminology_data_format

    out["Format"] = (
        aws_sdk_translate.types.terminology_data_format.serialize_aws_json_1_1(
            value["format"]
        )
    )
    if "directionality" in value:
        import aws_sdk_translate.types.directionality

        out["Directionality"] = (
            aws_sdk_translate.types.directionality.serialize_aws_json_1_1(
                value["directionality"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminologyData:
    out: TerminologyData = {}  # type: ignore[typeddict-item]
    if "File" in data:
        import aws_sdk_translate.types.terminology_file

        out["file"] = aws_sdk_translate.types.terminology_file.deserialize_aws_json_1_1(
            data["File"]
        )
    else:
        raise DeserializationError("TerminologyData.file required")
    if "Format" in data:
        import aws_sdk_translate.types.terminology_data_format

        out["format"] = (
            aws_sdk_translate.types.terminology_data_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        raise DeserializationError("TerminologyData.format required")
    if "Directionality" in data:
        import aws_sdk_translate.types.directionality

        out["directionality"] = (
            aws_sdk_translate.types.directionality.deserialize_aws_json_1_1(
                data["Directionality"]
            )
        )
    return out
