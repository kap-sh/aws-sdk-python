"""Generated from Smithy shape ``com.amazonaws.iot#Denied``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.explicit_deny
    import aws_sdk_iot.types.implicit_deny


class Denied(TypedDict):
    implicit_deny: NotRequired["aws_sdk_iot.types.implicit_deny.ImplicitDeny"]
    """<p>Information that implicitly denies the authorization. When a policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.</p>"""
    explicit_deny: NotRequired["aws_sdk_iot.types.explicit_deny.ExplicitDeny"]
    """<p>Information that explicitly denies the authorization. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Denied) -> dict:
    out: dict = {}
    if "implicit_deny" in value:
        import aws_sdk_iot.types.implicit_deny

        out["implicitDeny"] = aws_sdk_iot.types.implicit_deny.serialize_json(
            value["implicit_deny"]
        )
    if "explicit_deny" in value:
        import aws_sdk_iot.types.explicit_deny

        out["explicitDeny"] = aws_sdk_iot.types.explicit_deny.serialize_json(
            value["explicit_deny"]
        )
    return out


def deserialize_json(data: dict) -> Denied:
    out: Denied = {}  # type: ignore[typeddict-item]
    if "implicitDeny" in data:
        import aws_sdk_iot.types.implicit_deny

        out["implicit_deny"] = aws_sdk_iot.types.implicit_deny.deserialize_json(
            data["implicitDeny"]
        )
    if "explicitDeny" in data:
        import aws_sdk_iot.types.explicit_deny

        out["explicit_deny"] = aws_sdk_iot.types.explicit_deny.deserialize_json(
            data["explicitDeny"]
        )
    return out
