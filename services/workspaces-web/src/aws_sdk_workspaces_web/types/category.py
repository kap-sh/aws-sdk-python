"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Category``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

Category: TypeAlias = Literal[
    "Cults",
    "Gambling",
    "Nudity",
    "Pornography",
    "SexEducation",
    "Tasteless",
    "Violence",
    "DownloadSites",
    "ImageSharing",
    "PeerToPeer",
    "StreamingMediaAndDownloads",
    "GenerativeAI",
    "CriminalActivity",
    "Hacking",
    "HateAndIntolerance",
    "IllegalDrug",
    "IllegalSoftware",
    "SchoolCheating",
    "SelfHarm",
    "Weapons",
    "Chat",
    "Games",
    "InstantMessaging",
    "ProfessionalNetwork",
    "SocialNetworking",
    "WebBasedEmail",
    "ParkedDomains",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cults",
        "Gambling",
        "Nudity",
        "Pornography",
        "SexEducation",
        "Tasteless",
        "Violence",
        "DownloadSites",
        "ImageSharing",
        "PeerToPeer",
        "StreamingMediaAndDownloads",
        "GenerativeAI",
        "CriminalActivity",
        "Hacking",
        "HateAndIntolerance",
        "IllegalDrug",
        "IllegalSoftware",
        "SchoolCheating",
        "SelfHarm",
        "Weapons",
        "Chat",
        "Games",
        "InstantMessaging",
        "ProfessionalNetwork",
        "SocialNetworking",
        "WebBasedEmail",
        "ParkedDomains",
    )
)


def serialize_json(value: Category) -> str:
    return value


def deserialize_json(data: str) -> Category:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Category value: {data!r}")
    return cast(Category, data)
