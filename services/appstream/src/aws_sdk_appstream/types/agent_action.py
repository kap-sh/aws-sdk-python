"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>The type of agent action.</p> <ul> <li> <p>COMPUTER_VISION - Allows agents to take screenshots of the desktop.</p> </li> <li> <p>COMPUTER_INPUT - Allows agents to click, type, and scroll on the desktop. Requires COMPUTER_VISION to also be enabled.</p> </li> </ul>"""
AgentAction: TypeAlias = Literal[
    "COMPUTER_VISION",
    "COMPUTER_INPUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPUTER_VISION",
        "COMPUTER_INPUT",
    )
)


def serialize_aws_json_1_1(value: AgentAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentAction value: {data!r}")
    return cast(AgentAction, data)
