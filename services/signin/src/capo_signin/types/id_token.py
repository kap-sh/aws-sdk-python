"""Generated from Smithy shape ``com.amazonaws.signin#IdToken``."""

from typing import TypeAlias

"""ID token containing user identity information Encoded JWT token containing user identity claims and authentication context. Returned only in authorization code redemption responses (grant_type=authorization_code). Contains user identity information such as ARN and other identity claims."""
IdToken: TypeAlias = str
