"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_enum_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.locale_type
    import aws_sdk_workdocs.types.storage_rule_type
    import aws_sdk_workdocs.types.time_zone_id_type
    import aws_sdk_workdocs.types.user_attribute_value_type
    import aws_sdk_workdocs.types.user_type


class UpdateUserRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    user_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the user.</p>"""
    given_name: NotRequired[
        "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user.</p>"""
    surname: NotRequired[
        "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    type: NotRequired["aws_sdk_workdocs.types.user_type.UserType"]
    """<p>The type of the user.</p>"""
    storage_rule: NotRequired[
        "aws_sdk_workdocs.types.storage_rule_type.StorageRuleType"
    ]
    """<p>The amount of storage for the user.</p>"""
    time_zone_id: NotRequired["aws_sdk_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    locale: NotRequired["aws_sdk_workdocs.types.locale_type.LocaleType"]
    """<p>The locale of the user.</p>"""
    grant_poweruser_privileges: NotRequired[
        "aws_sdk_workdocs.types.boolean_enum_type.BooleanEnumType"
    ]
    """<p>Boolean value to determine whether the user is granted Power user privileges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "type" in value:
        import aws_sdk_workdocs.types.user_type

        out["Type"] = aws_sdk_workdocs.types.user_type.serialize_json(value["type"])
    if "storage_rule" in value:
        import aws_sdk_workdocs.types.storage_rule_type

        out["StorageRule"] = aws_sdk_workdocs.types.storage_rule_type.serialize_json(
            value["storage_rule"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "locale" in value:
        import aws_sdk_workdocs.types.locale_type

        out["Locale"] = aws_sdk_workdocs.types.locale_type.serialize_json(
            value["locale"]
        )
    if "grant_poweruser_privileges" in value:
        import aws_sdk_workdocs.types.boolean_enum_type

        out["GrantPoweruserPrivileges"] = (
            aws_sdk_workdocs.types.boolean_enum_type.serialize_json(
                value["grant_poweruser_privileges"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "Type" in data:
        import aws_sdk_workdocs.types.user_type

        out["type"] = aws_sdk_workdocs.types.user_type.deserialize_json(data["Type"])
    if "StorageRule" in data:
        import aws_sdk_workdocs.types.storage_rule_type

        out["storage_rule"] = aws_sdk_workdocs.types.storage_rule_type.deserialize_json(
            data["StorageRule"]
        )
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    if "Locale" in data:
        import aws_sdk_workdocs.types.locale_type

        out["locale"] = aws_sdk_workdocs.types.locale_type.deserialize_json(
            data["Locale"]
        )
    if "GrantPoweruserPrivileges" in data:
        import aws_sdk_workdocs.types.boolean_enum_type

        out["grant_poweruser_privileges"] = (
            aws_sdk_workdocs.types.boolean_enum_type.deserialize_json(
                data["GrantPoweruserPrivileges"]
            )
        )
    return out
