"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarTagValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.boolean_attribute
    import capo_verifiedpermissions.types.cedar_tag_record_attribute
    import capo_verifiedpermissions.types.cedar_tag_set_attribute
    import capo_verifiedpermissions.types.datetime_attribute
    import capo_verifiedpermissions.types.decimal
    import capo_verifiedpermissions.types.duration
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.ip_addr
    import capo_verifiedpermissions.types.long_attribute
    import capo_verifiedpermissions.types.string_attribute


class _CedarTagValue_boolean(TypedDict, closed=True):
    boolean: "capo_verifiedpermissions.types.boolean_attribute.BooleanAttribute"


class _CedarTagValue_entityIdentifier(TypedDict, closed=True):
    entityIdentifier: (
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    )


class _CedarTagValue_long(TypedDict, closed=True):
    long: "capo_verifiedpermissions.types.long_attribute.LongAttribute"


class _CedarTagValue_string(TypedDict, closed=True):
    string: "capo_verifiedpermissions.types.string_attribute.StringAttribute"


class _CedarTagValue_set(TypedDict, closed=True):
    set: "capo_verifiedpermissions.types.cedar_tag_set_attribute.CedarTagSetAttribute"


class _CedarTagValue_record(TypedDict, closed=True):
    record: "capo_verifiedpermissions.types.cedar_tag_record_attribute.CedarTagRecordAttribute"


class _CedarTagValue_ipaddr(TypedDict, closed=True):
    ipaddr: "capo_verifiedpermissions.types.ip_addr.IpAddr"


class _CedarTagValue_decimal(TypedDict, closed=True):
    decimal: "capo_verifiedpermissions.types.decimal.Decimal"


class _CedarTagValue_datetime(TypedDict, closed=True):
    datetime: "capo_verifiedpermissions.types.datetime_attribute.DatetimeAttribute"


class _CedarTagValue_duration(TypedDict, closed=True):
    duration: "capo_verifiedpermissions.types.duration.Duration"


CedarTagValue: TypeAlias = (
    _CedarTagValue_boolean
    | _CedarTagValue_entityIdentifier
    | _CedarTagValue_long
    | _CedarTagValue_string
    | _CedarTagValue_set
    | _CedarTagValue_record
    | _CedarTagValue_ipaddr
    | _CedarTagValue_decimal
    | _CedarTagValue_datetime
    | _CedarTagValue_duration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CedarTagValue) -> dict:
    if "boolean" in value:
        return {"boolean": value["boolean"]}
    elif "entityIdentifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "entityIdentifier": capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["entityIdentifier"]
            )
        }
    elif "long" in value:
        return {"long": value["long"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "set" in value:
        import capo_verifiedpermissions.types.cedar_tag_set_attribute

        return {
            "set": capo_verifiedpermissions.types.cedar_tag_set_attribute.serialize_aws_json_1_0(
                value["set"]
            )
        }
    elif "record" in value:
        import capo_verifiedpermissions.types.cedar_tag_record_attribute

        return {
            "record": capo_verifiedpermissions.types.cedar_tag_record_attribute.serialize_aws_json_1_0(
                value["record"]
            )
        }
    elif "ipaddr" in value:
        return {"ipaddr": value["ipaddr"]}
    elif "decimal" in value:
        return {"decimal": value["decimal"]}
    elif "datetime" in value:
        return {"datetime": value["datetime"]}
    elif "duration" in value:
        return {"duration": value["duration"]}
    else:
        raise SerializationError("CedarTagValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> CedarTagValue:
    if "boolean" in data:
        return {"boolean": data["boolean"]}
    elif "entityIdentifier" in data:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "entityIdentifier": capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["entityIdentifier"]
            )
        }
    elif "long" in data:
        return {"long": data["long"]}
    elif "string" in data:
        return {"string": data["string"]}
    elif "set" in data:
        import capo_verifiedpermissions.types.cedar_tag_set_attribute

        return {
            "set": capo_verifiedpermissions.types.cedar_tag_set_attribute.deserialize_aws_json_1_0(
                data["set"]
            )
        }
    elif "record" in data:
        import capo_verifiedpermissions.types.cedar_tag_record_attribute

        return {
            "record": capo_verifiedpermissions.types.cedar_tag_record_attribute.deserialize_aws_json_1_0(
                data["record"]
            )
        }
    elif "ipaddr" in data:
        return {"ipaddr": data["ipaddr"]}
    elif "decimal" in data:
        return {"decimal": data["decimal"]}
    elif "datetime" in data:
        return {"datetime": data["datetime"]}
    elif "duration" in data:
        return {"duration": data["duration"]}
    else:
        raise DeserializationError("CedarTagValue: no recognized variant key")
