"""Generated from Smithy shape ``com.amazonaws.acm#X509AttributeFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.extended_key_usage_name
    import aws_sdk_acm.types.key_algorithm
    import aws_sdk_acm.types.key_usage_name
    import aws_sdk_acm.types.serial_number
    import aws_sdk_acm.types.subject_alternative_name_filter
    import aws_sdk_acm.types.subject_filter
    import aws_sdk_acm.types.timestamp_range


class _X509AttributeFilter_Subject(TypedDict):
    Subject: "aws_sdk_acm.types.subject_filter.SubjectFilter"


class _X509AttributeFilter_SubjectAlternativeName(TypedDict):
    SubjectAlternativeName: (
        "aws_sdk_acm.types.subject_alternative_name_filter.SubjectAlternativeNameFilter"
    )


class _X509AttributeFilter_ExtendedKeyUsage(TypedDict):
    ExtendedKeyUsage: "aws_sdk_acm.types.extended_key_usage_name.ExtendedKeyUsageName"


class _X509AttributeFilter_KeyUsage(TypedDict):
    KeyUsage: "aws_sdk_acm.types.key_usage_name.KeyUsageName"


class _X509AttributeFilter_KeyAlgorithm(TypedDict):
    KeyAlgorithm: "aws_sdk_acm.types.key_algorithm.KeyAlgorithm"


class _X509AttributeFilter_SerialNumber(TypedDict):
    SerialNumber: "aws_sdk_acm.types.serial_number.SerialNumber"


class _X509AttributeFilter_NotAfter(TypedDict):
    NotAfter: "aws_sdk_acm.types.timestamp_range.TimestampRange"


class _X509AttributeFilter_NotBefore(TypedDict):
    NotBefore: "aws_sdk_acm.types.timestamp_range.TimestampRange"


X509AttributeFilter: TypeAlias = (
    _X509AttributeFilter_Subject
    | _X509AttributeFilter_SubjectAlternativeName
    | _X509AttributeFilter_ExtendedKeyUsage
    | _X509AttributeFilter_KeyUsage
    | _X509AttributeFilter_KeyAlgorithm
    | _X509AttributeFilter_SerialNumber
    | _X509AttributeFilter_NotAfter
    | _X509AttributeFilter_NotBefore
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: X509AttributeFilter) -> dict:
    if "Subject" in value:
        import aws_sdk_acm.types.subject_filter

        return {
            "Subject": aws_sdk_acm.types.subject_filter.serialize_aws_json_1_1(
                value["Subject"]
            )
        }
    elif "SubjectAlternativeName" in value:
        import aws_sdk_acm.types.subject_alternative_name_filter

        return {
            "SubjectAlternativeName": aws_sdk_acm.types.subject_alternative_name_filter.serialize_aws_json_1_1(
                value["SubjectAlternativeName"]
            )
        }
    elif "ExtendedKeyUsage" in value:
        import aws_sdk_acm.types.extended_key_usage_name

        return {
            "ExtendedKeyUsage": aws_sdk_acm.types.extended_key_usage_name.serialize_aws_json_1_1(
                value["ExtendedKeyUsage"]
            )
        }
    elif "KeyUsage" in value:
        import aws_sdk_acm.types.key_usage_name

        return {
            "KeyUsage": aws_sdk_acm.types.key_usage_name.serialize_aws_json_1_1(
                value["KeyUsage"]
            )
        }
    elif "KeyAlgorithm" in value:
        import aws_sdk_acm.types.key_algorithm

        return {
            "KeyAlgorithm": aws_sdk_acm.types.key_algorithm.serialize_aws_json_1_1(
                value["KeyAlgorithm"]
            )
        }
    elif "SerialNumber" in value:
        return {"SerialNumber": value["SerialNumber"]}
    elif "NotAfter" in value:
        import aws_sdk_acm.types.timestamp_range

        return {
            "NotAfter": aws_sdk_acm.types.timestamp_range.serialize_aws_json_1_1(
                value["NotAfter"]
            )
        }
    elif "NotBefore" in value:
        import aws_sdk_acm.types.timestamp_range

        return {
            "NotBefore": aws_sdk_acm.types.timestamp_range.serialize_aws_json_1_1(
                value["NotBefore"]
            )
        }
    else:
        raise SerializationError("X509AttributeFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> X509AttributeFilter:
    if "Subject" in data:
        import aws_sdk_acm.types.subject_filter

        return {
            "Subject": aws_sdk_acm.types.subject_filter.deserialize_aws_json_1_1(
                data["Subject"]
            )
        }
    elif "SubjectAlternativeName" in data:
        import aws_sdk_acm.types.subject_alternative_name_filter

        return {
            "SubjectAlternativeName": aws_sdk_acm.types.subject_alternative_name_filter.deserialize_aws_json_1_1(
                data["SubjectAlternativeName"]
            )
        }
    elif "ExtendedKeyUsage" in data:
        import aws_sdk_acm.types.extended_key_usage_name

        return {
            "ExtendedKeyUsage": aws_sdk_acm.types.extended_key_usage_name.deserialize_aws_json_1_1(
                data["ExtendedKeyUsage"]
            )
        }
    elif "KeyUsage" in data:
        import aws_sdk_acm.types.key_usage_name

        return {
            "KeyUsage": aws_sdk_acm.types.key_usage_name.deserialize_aws_json_1_1(
                data["KeyUsage"]
            )
        }
    elif "KeyAlgorithm" in data:
        import aws_sdk_acm.types.key_algorithm

        return {
            "KeyAlgorithm": aws_sdk_acm.types.key_algorithm.deserialize_aws_json_1_1(
                data["KeyAlgorithm"]
            )
        }
    elif "SerialNumber" in data:
        return {"SerialNumber": data["SerialNumber"]}
    elif "NotAfter" in data:
        import aws_sdk_acm.types.timestamp_range

        return {
            "NotAfter": aws_sdk_acm.types.timestamp_range.deserialize_aws_json_1_1(
                data["NotAfter"]
            )
        }
    elif "NotBefore" in data:
        import aws_sdk_acm.types.timestamp_range

        return {
            "NotBefore": aws_sdk_acm.types.timestamp_range.deserialize_aws_json_1_1(
                data["NotBefore"]
            )
        }
    else:
        raise DeserializationError("X509AttributeFilter: no recognized variant key")
