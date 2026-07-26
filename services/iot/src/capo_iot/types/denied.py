"""Generated from Smithy shape ``com.amazonaws.iot#Denied``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.explicit_deny
    import capo_iot.types.implicit_deny


class Denied(TypedDict, closed=True):
    implicit_deny: NotRequired["capo_iot.types.implicit_deny.ImplicitDeny"]
    """<p>Information that implicitly denies the authorization. When a policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.</p>"""
    explicit_deny: NotRequired["capo_iot.types.explicit_deny.ExplicitDeny"]
    """<p>Information that explicitly denies the authorization. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Denied) -> dict:
    out: dict = {}
    if "implicit_deny" in value:
        import capo_iot.types.implicit_deny

        out["implicitDeny"] = capo_iot.types.implicit_deny.serialize_json(
            value["implicit_deny"]
        )
    if "explicit_deny" in value:
        import capo_iot.types.explicit_deny

        out["explicitDeny"] = capo_iot.types.explicit_deny.serialize_json(
            value["explicit_deny"]
        )
    return out


def deserialize_json(data: dict) -> Denied:
    out: Denied = {}  # type: ignore[typeddict-item]
    if "implicitDeny" in data:
        import capo_iot.types.implicit_deny

        out["implicit_deny"] = capo_iot.types.implicit_deny.deserialize_json(
            data["implicitDeny"]
        )
    if "explicitDeny" in data:
        import capo_iot.types.explicit_deny

        out["explicit_deny"] = capo_iot.types.explicit_deny.deserialize_json(
            data["explicitDeny"]
        )
    return out
