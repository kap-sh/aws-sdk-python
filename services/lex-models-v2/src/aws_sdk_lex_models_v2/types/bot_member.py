"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_name
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name


class BotMember(TypedDict, closed=True):
    bot_member_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique ID of a bot that is a member of this network of bots.</p>"""
    bot_member_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The unique name of a bot that is a member of this network of bots.</p>"""
    bot_member_alias_id: "aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The alias ID of a bot that is a member of this network of bots.</p>"""
    bot_member_alias_name: "aws_sdk_lex_models_v2.types.bot_alias_name.BotAliasName"
    """<p>The alias name of a bot that is a member of this network of bots.</p>"""
    bot_member_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of a bot that is a member of this network of bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotMember) -> dict:
    out: dict = {}
    out["botMemberId"] = value["bot_member_id"]
    out["botMemberName"] = value["bot_member_name"]
    out["botMemberAliasId"] = value["bot_member_alias_id"]
    out["botMemberAliasName"] = value["bot_member_alias_name"]
    out["botMemberVersion"] = value["bot_member_version"]
    return out


def deserialize_json(data: dict) -> BotMember:
    out: BotMember = {}  # type: ignore[typeddict-item]
    if "botMemberId" in data:
        out["bot_member_id"] = data["botMemberId"]
    else:
        raise DeserializationError("BotMember.bot_member_id required")
    if "botMemberName" in data:
        out["bot_member_name"] = data["botMemberName"]
    else:
        raise DeserializationError("BotMember.bot_member_name required")
    if "botMemberAliasId" in data:
        out["bot_member_alias_id"] = data["botMemberAliasId"]
    else:
        raise DeserializationError("BotMember.bot_member_alias_id required")
    if "botMemberAliasName" in data:
        out["bot_member_alias_name"] = data["botMemberAliasName"]
    else:
        raise DeserializationError("BotMember.bot_member_alias_name required")
    if "botMemberVersion" in data:
        out["bot_member_version"] = data["botMemberVersion"]
    else:
        raise DeserializationError("BotMember.bot_member_version required")
    return out
