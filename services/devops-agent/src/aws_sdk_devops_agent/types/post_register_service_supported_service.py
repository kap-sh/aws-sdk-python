"""Generated from Smithy shape ``com.amazonaws.devopsagent#PostRegisterServiceSupportedService``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Services that can be registered via the post-registration API (excludes OAuth 3LO services).</p>"""
PostRegisterServiceSupportedService: TypeAlias = Literal[
    "dynatrace",
    "servicenow",
    "pagerduty",
    "gitlab",
    "eventChannel",
    "mcpservernewrelic",
    "mcpservergrafana",
    "mcpserverdatadog",
    "mcpserver",
    "mcpserversplunk",
    "azureidentity",
    "mcpserversigv4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "dynatrace",
        "servicenow",
        "pagerduty",
        "gitlab",
        "eventChannel",
        "mcpservernewrelic",
        "mcpservergrafana",
        "mcpserverdatadog",
        "mcpserver",
        "mcpserversplunk",
        "azureidentity",
        "mcpserversigv4",
    )
)


def serialize_json(value: PostRegisterServiceSupportedService) -> str:
    return value


def deserialize_json(data: str) -> PostRegisterServiceSupportedService:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PostRegisterServiceSupportedService value: {data!r}"
        )
    return cast(PostRegisterServiceSupportedService, data)
