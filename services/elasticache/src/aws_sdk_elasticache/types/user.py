"""Generated from Smithy shape ``com.amazonaws.elasticache#User``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.authentication
    import aws_sdk_elasticache.types.engine_type
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.user_group_id_list


class User(TypedDict):
    user_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the user.</p>"""
    user_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The username of the user.</p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    r"""<p>Indicates the user status. Can be \"active\", \"modifying\" or \"deleting\".</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.engine_type.EngineType"]
    """<p>The options are valkey or redis.</p>"""
    minimum_engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The minimum engine version required, which is Redis OSS 6.0</p>"""
    access_string: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Access permissions string used for this user.</p>"""
    user_group_ids: NotRequired[
        "aws_sdk_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>Returns a list of the user group IDs the user belongs to.</p>"""
    authentication: NotRequired[
        "aws_sdk_elasticache.types.authentication.Authentication"
    ]
    """<p>Denotes whether the user requires a password to authenticate.</p>"""
    arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: User, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{prefix}.MinimumEngineVersion", str(value["minimum_engine_version"]))
        )
    if "access_string" in value:
        pairs.append((f"{prefix}.AccessString", str(value["access_string"])))
    if "user_group_ids" in value:
        import aws_sdk_elasticache.types.user_group_id_list

        aws_sdk_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids"], pairs, f"{prefix}.UserGroupIds"
        )
    if "authentication" in value:
        import aws_sdk_elasticache.types.authentication

        aws_sdk_elasticache.types.authentication.serialize_query(
            value["authentication"], pairs, f"{prefix}.Authentication"
        )
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))


def deserialize_query(el: Element) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    child_access_string = el.find("AccessString")
    if child_access_string is not None:
        out["access_string"] = str(child_access_string.text or "")
    child_user_group_ids = el.find("UserGroupIds")
    if child_user_group_ids is not None:
        import aws_sdk_elasticache.types.user_group_id_list

        out["user_group_ids"] = (
            aws_sdk_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids
            )
        )
    child_authentication = el.find("Authentication")
    if child_authentication is not None:
        import aws_sdk_elasticache.types.authentication

        out["authentication"] = (
            aws_sdk_elasticache.types.authentication.deserialize_query(
                child_authentication
            )
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
