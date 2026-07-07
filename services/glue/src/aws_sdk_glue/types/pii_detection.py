"""Generated from Smithy shape ``com.amazonaws.glue#PIIDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_double_fraction
    import aws_sdk_glue.types.boxed_positive_int
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.mask_value
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.pii_type


class PIIDetection(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The node ID inputs to the transform.</p>"""
    pii_type: "aws_sdk_glue.types.pii_type.PiiType"
    """<p>Indicates the type of PIIDetection transform. </p>"""
    entity_types_to_detect: (
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>Indicates the types of entities the PIIDetection transform will identify as PII data. </p> <p> PII type entities include: PERSON_NAME, DATE, USA_SNN, EMAIL, USA_ITIN, USA_PASSPORT_NUMBER, PHONE_NUMBER, BANK_ACCOUNT, IP_ADDRESS, MAC_ADDRESS, USA_CPT_CODE, USA_HCPCS_CODE, USA_NATIONAL_DRUG_CODE, USA_MEDICARE_BENEFICIARY_IDENTIFIER, USA_HEALTH_INSURANCE_CLAIM_NUMBER,CREDIT_CARD,USA_NATIONAL_PROVIDER_IDENTIFIER,USA_DEA_NUMBER,USA_DRIVING_LICENSE </p>"""
    output_column_name: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Indicates the output column name that will contain any entity type detected in that row. </p>"""
    sample_fraction: NotRequired[
        "aws_sdk_glue.types.boxed_double_fraction.BoxedDoubleFraction"
    ]
    """<p>Indicates the fraction of the data to sample when scanning for PII entities. </p>"""
    threshold_fraction: NotRequired[
        "aws_sdk_glue.types.boxed_double_fraction.BoxedDoubleFraction"
    ]
    """<p>Indicates the fraction of the data that must be met in order for a column to be identified as PII data. </p>"""
    mask_value: NotRequired["aws_sdk_glue.types.mask_value.MaskValue"]
    """<p>Indicates the value that will replace the detected entity. </p>"""
    redact_text: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies whether to redact the detected PII text. When set to <code>true</code>, PII content is replaced with redaction characters.</p>"""
    redact_char: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The character used to replace detected PII content when redaction is enabled. The default redaction character is <code>*</code>.</p>"""
    match_pattern: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>A regular expression pattern used to identify additional PII content beyond the standard detection algorithms.</p>"""
    num_left_chars_to_exclude: NotRequired[
        "aws_sdk_glue.types.boxed_positive_int.BoxedPositiveInt"
    ]
    """<p>The number of characters to exclude from redaction on the left side of detected PII content. This allows preserving context around the sensitive data.</p>"""
    num_right_chars_to_exclude: NotRequired[
        "aws_sdk_glue.types.boxed_positive_int.BoxedPositiveInt"
    ]
    """<p>The number of characters to exclude from redaction on the right side of detected PII content. This allows preserving context around the sensitive data.</p>"""
    detection_parameters: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Additional parameters for configuring PII detection behavior and sensitivity settings.</p>"""
    detection_sensitivity: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The sensitivity level for PII detection. Higher sensitivity levels detect more potential PII but may result in more false positives.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PIIDetection) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import aws_sdk_glue.types.pii_type

    out["PiiType"] = aws_sdk_glue.types.pii_type.serialize_aws_json_1_1(
        value["pii_type"]
    )
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["EntityTypesToDetect"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["entity_types_to_detect"]
        )
    )
    if "output_column_name" in value:
        out["OutputColumnName"] = value["output_column_name"]
    if "sample_fraction" in value:
        out["SampleFraction"] = value["sample_fraction"]
    if "threshold_fraction" in value:
        out["ThresholdFraction"] = value["threshold_fraction"]
    if "mask_value" in value:
        out["MaskValue"] = value["mask_value"]
    if "redact_text" in value:
        out["RedactText"] = value["redact_text"]
    if "redact_char" in value:
        out["RedactChar"] = value["redact_char"]
    if "match_pattern" in value:
        out["MatchPattern"] = value["match_pattern"]
    if "num_left_chars_to_exclude" in value:
        out["NumLeftCharsToExclude"] = value["num_left_chars_to_exclude"]
    if "num_right_chars_to_exclude" in value:
        out["NumRightCharsToExclude"] = value["num_right_chars_to_exclude"]
    if "detection_parameters" in value:
        out["DetectionParameters"] = value["detection_parameters"]
    if "detection_sensitivity" in value:
        out["DetectionSensitivity"] = value["detection_sensitivity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PIIDetection:
    out: PIIDetection = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PIIDetection.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("PIIDetection.inputs required")
    if "PiiType" in data:
        import aws_sdk_glue.types.pii_type

        out["pii_type"] = aws_sdk_glue.types.pii_type.deserialize_aws_json_1_1(
            data["PiiType"]
        )
    else:
        raise DeserializationError("PIIDetection.pii_type required")
    if "EntityTypesToDetect" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["entity_types_to_detect"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["EntityTypesToDetect"]
            )
        )
    else:
        raise DeserializationError("PIIDetection.entity_types_to_detect required")
    if "OutputColumnName" in data:
        out["output_column_name"] = data["OutputColumnName"]
    if "SampleFraction" in data:
        out["sample_fraction"] = data["SampleFraction"]
    if "ThresholdFraction" in data:
        out["threshold_fraction"] = data["ThresholdFraction"]
    if "MaskValue" in data:
        out["mask_value"] = data["MaskValue"]
    if "RedactText" in data:
        out["redact_text"] = data["RedactText"]
    if "RedactChar" in data:
        out["redact_char"] = data["RedactChar"]
    if "MatchPattern" in data:
        out["match_pattern"] = data["MatchPattern"]
    if "NumLeftCharsToExclude" in data:
        out["num_left_chars_to_exclude"] = data["NumLeftCharsToExclude"]
    if "NumRightCharsToExclude" in data:
        out["num_right_chars_to_exclude"] = data["NumRightCharsToExclude"]
    if "DetectionParameters" in data:
        out["detection_parameters"] = data["DetectionParameters"]
    if "DetectionSensitivity" in data:
        out["detection_sensitivity"] = data["DetectionSensitivity"]
    return out
