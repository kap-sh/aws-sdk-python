"""Generated from Smithy shape ``com.amazonaws.acm#GeneralName``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.distinguished_name
    import aws_sdk_acm.types.other_name
    import aws_sdk_acm.types.string


class _GeneralName_DirectoryName(TypedDict, closed=True):
    DirectoryName: "aws_sdk_acm.types.distinguished_name.DistinguishedName"


class _GeneralName_DnsName(TypedDict, closed=True):
    DnsName: "aws_sdk_acm.types.string.String"


class _GeneralName_IpAddress(TypedDict, closed=True):
    IpAddress: "aws_sdk_acm.types.string.String"


class _GeneralName_OtherName(TypedDict, closed=True):
    OtherName: "aws_sdk_acm.types.other_name.OtherName"


class _GeneralName_RegisteredId(TypedDict, closed=True):
    RegisteredId: "aws_sdk_acm.types.string.String"


class _GeneralName_Rfc822Name(TypedDict, closed=True):
    Rfc822Name: "aws_sdk_acm.types.string.String"


class _GeneralName_UniformResourceIdentifier(TypedDict, closed=True):
    UniformResourceIdentifier: "aws_sdk_acm.types.string.String"


GeneralName: TypeAlias = (
    _GeneralName_DirectoryName
    | _GeneralName_DnsName
    | _GeneralName_IpAddress
    | _GeneralName_OtherName
    | _GeneralName_RegisteredId
    | _GeneralName_Rfc822Name
    | _GeneralName_UniformResourceIdentifier
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralName) -> dict:
    if "DirectoryName" in value:
        import aws_sdk_acm.types.distinguished_name

        return {
            "DirectoryName": aws_sdk_acm.types.distinguished_name.serialize_aws_json_1_1(
                value["DirectoryName"]
            )
        }
    elif "DnsName" in value:
        return {"DnsName": value["DnsName"]}
    elif "IpAddress" in value:
        return {"IpAddress": value["IpAddress"]}
    elif "OtherName" in value:
        import aws_sdk_acm.types.other_name

        return {
            "OtherName": aws_sdk_acm.types.other_name.serialize_aws_json_1_1(
                value["OtherName"]
            )
        }
    elif "RegisteredId" in value:
        return {"RegisteredId": value["RegisteredId"]}
    elif "Rfc822Name" in value:
        return {"Rfc822Name": value["Rfc822Name"]}
    elif "UniformResourceIdentifier" in value:
        return {"UniformResourceIdentifier": value["UniformResourceIdentifier"]}
    else:
        raise SerializationError("GeneralName: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GeneralName:
    if "DirectoryName" in data:
        import aws_sdk_acm.types.distinguished_name

        return {
            "DirectoryName": aws_sdk_acm.types.distinguished_name.deserialize_aws_json_1_1(
                data["DirectoryName"]
            )
        }
    elif "DnsName" in data:
        return {"DnsName": data["DnsName"]}
    elif "IpAddress" in data:
        return {"IpAddress": data["IpAddress"]}
    elif "OtherName" in data:
        import aws_sdk_acm.types.other_name

        return {
            "OtherName": aws_sdk_acm.types.other_name.deserialize_aws_json_1_1(
                data["OtherName"]
            )
        }
    elif "RegisteredId" in data:
        return {"RegisteredId": data["RegisteredId"]}
    elif "Rfc822Name" in data:
        return {"Rfc822Name": data["Rfc822Name"]}
    elif "UniformResourceIdentifier" in data:
        return {"UniformResourceIdentifier": data["UniformResourceIdentifier"]}
    else:
        raise DeserializationError("GeneralName: no recognized variant key")
