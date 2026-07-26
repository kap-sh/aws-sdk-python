"""Generated from Smithy shape ``com.amazonaws.autoscaling#SetInstanceProtectionAnswer``."""

from typing_extensions import TypedDict

from capo_auto_scaling._protocol.xml import Element


class SetInstanceProtectionAnswer(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetInstanceProtectionAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetInstanceProtectionAnswer:
    out: SetInstanceProtectionAnswer = {}  # type: ignore[typeddict-item]
    return out
